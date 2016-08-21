var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

// redis 链接
var redis   = require('redis');
var client  = redis.createClient('6379', '127.0.0.1');

// redis 链接错误
client.on("error", function(error) {
		console.log(error);
});

//redis准备完毕
client.on('ready',function(err){
    console.log('ready');
});

//服务器应答
app.get('/', function(req, res){
		res.send('<h1>Welcome Realtime Server</h1>');
		});

//在线用户
var onlineUsers = {};
//当前在线人数
var onlineCount = 0;
//发送消息条数
var messageCount = 0;
//消息队列推送数
var messagePushCount = 10;

io.on('connection', function(socket){
		console.log('a user connected');

		//监听新用户加入
		socket.on('login', function(obj){
			//将新加入用户的唯一标识当作socket的名称，后面退出的时候会用到
			socket.name = obj.userid;

			//检查在线列表，如果不在里面就加入
			if(!onlineUsers.hasOwnProperty(obj.userid)) {
			onlineUsers[obj.userid] = obj.username;
			//在线人数+1
			onlineCount++;
			}

			//向所有客户端广播用户加入
			io.emit('login', {onlineUsers:onlineUsers, onlineCount:onlineCount, user:obj});

			for(var i = messageCount - messagePushCount; i <= messageCount; i++) {
				client.hgetall(i, function(err, reply) {
					if(!isEmpty(reply)) {
						//用户id
						console.log(reply.id);
						//用户昵称
						console.log(reply.name);
						//消息内容
						console.log(reply.content);
						//向新加入的用户推送之前的消息
						io.sockets.connected[socket.id].emit('message', {userid:reply.id, username:reply.name, content:reply.content});
					}
				});
			}

			console.log(obj.username+'加入了聊天室');
			});

		//监听用户退出
		socket.on('disconnect', function(){
			//将退出的用户从在线列表中删除
			if(onlineUsers.hasOwnProperty(socket.name)) {
				//退出用户的信息
				var obj = {userid:socket.name, username:onlineUsers[socket.name]};

				//删除
				delete onlineUsers[socket.name];
				//在线人数-1
				onlineCount--;

				//向所有客户端广播用户退出
				io.emit('logout', {onlineUsers:onlineUsers, onlineCount:onlineCount, user:obj});
				console.log(obj.username+'退出了聊天室');
			}
		});

		//监听用户发布聊天内容
		socket.on('message', function(obj){
			//向所有客户端广播发布的消息
			io.emit('message', obj);
			console.log(obj.username+'说：'+obj.content);
			
			//增加消息计数
			messageCount += 1;
			console.log(messageCount);

			//写入redis
			client.hmset(messageCount, {'id':obj.userid,'name':obj.username,'content':obj.content}, redis.print);
		});

	});

//监听端口
http.listen(3000, function(){
		console.log('listening on *:3000');
		});

//判断对象是否为空
function isEmpty(obj) {
	for (var name in obj) {
		return false;
	}
	return true;
};
