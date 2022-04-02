```shell
#create conda  viture  environment
conda create -y -n pyarrow_pandas_env3.6 python=3.6  pandas pyarrow
````

```shell
#activate env
conda activate pyarrow_pandas_env365
```

```shell
#package customized env
conda pack -n pyarrow_pandas_env365 -o pyarrow_pandas_env365.tar.gz
```

```shell
#upload file package to hadoop
hadoop fs -put pyarrow_pandas_env365.tar.gz /user/b_aip/jialesun/
```
