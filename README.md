# blog_app
responsive django personal blog app


#### how to use:
```virtualenv```
```python
$ virtualenv <env_name>
$ source <env_name>/bin/activate
(<env_name>) $ pip install -r path/to/requirements.txt

from project folder:

(<env_name>) $ python3 manage.py runserver
```

or via ```Docker```:

```shell
$ docker-compose up --build
```
alternatively, if you have a container already build-up:

```shell
$ docker-compose up
```
project will then be available at these hosts under port ```8000```:

![image](https://user-images.githubusercontent.com/25802489/208301942-dd07d8be-acc8-4a7a-baa9-130fa62e1fb2.png)


to load up test data from fixtures run this from project root directory:
```shell
$ python3 manage.py loaddata initial_data.json
```
#### functionality:

##### create, read:
![new_topic](https://user-images.githubusercontent.com/25802489/208301275-1826b78b-165a-4715-8834-3599c9f14481.gif)
![read_topic](https://user-images.githubusercontent.com/25802489/208301336-81084f46-b12d-4a7e-b9d0-67a4db39e962.gif)

##### update, delete:
###### can be hidden and managed only from admin
![topic_update](https://user-images.githubusercontent.com/25802489/208301367-820aad5f-4904-41eb-ad18-f2d2dd94881c.gif)
![topic_delete](https://user-images.githubusercontent.com/25802489/208301370-27c459ad-cf55-49f3-b99d-5e1f3a73c444.gif)

##### search topics by click on tags:
![search_by_tags](https://user-images.githubusercontent.com/25802489/208301406-ac47ddee-fdde-4a88-a172-cac7433f163f.gif)

#### Rest API:
![image](https://user-images.githubusercontent.com/25802489/208303429-e0b922be-fdf2-4020-a21b-7e8c0ff1b3c0.png)
![photo_2022-12-18_14-40-32](https://user-images.githubusercontent.com/25802489/208301533-26ddaa91-4d24-4c64-b39d-27b3dc70d29c.jpg)

#### admin:
![image](https://user-images.githubusercontent.com/25802489/208301701-a432f5c0-6ead-4729-839e-8335ce5262d8.png)
