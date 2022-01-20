1、Linux安装libzmq3-dev
2、编译server.cpp

```
g++ -g -Wall server.cpp -o server -lstdc++ -lzmq
```

3、运行sever

```
./server
```

4、运行client

```
python3 client.py
```

