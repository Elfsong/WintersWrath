#coding = utf-8
import my_pb2

if __name__ == "__main__":
	test1 = my_pb2.Person()
	test1.id = 1
	test1.testname = "Erik"
	out = test1.SerializeToString()

#	test2 = my_pb2.Person()
#	test_obj = test2.FromString(out)
#	print test_obj.id,test_obj.testname
	print out
