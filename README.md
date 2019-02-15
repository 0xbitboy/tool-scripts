# tool-scripts

## 环境
- python 3.x
- 安装依赖
```
pip install -r requirements.txt
```


## 脚本说明

- redis-key-scan-by-pattern.py 根据通配符扫描所有KEY
```
usage: redis-key-scan-by-pattern.py [-h] --host HOST [--port PORT] 
                                   pattern batch_size
```
- redis-set_ttl_by_pattern.py 给符合通配符的KEY设置一个过期时间

```
usage: redis-set_ttl_by_pattern.py [-h] --host HOST [--port PORT]
                                   pattern ttl [ttl ...]
```
```
eg. 扫描test_expire:*的所有key，并设置一个1000 到2000秒的随机过期时间
$ python redis-set_ttl_by_pattern.py --host localhost "test_expire:*" 1000 2000
```
