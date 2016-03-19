# get final url
python final_url.py

cat ./output | while read LINE
do
    echo $LINE
    name=`echo "$LINE" | awk -F'[/:]' '{print $4}'`
    echo $name
    phantomjs test.js $LINE pic/$name.png
done


