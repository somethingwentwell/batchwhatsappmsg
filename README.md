# batchwhatsappmsg
## SET UP ENVIRONMENT
### Pull Docker images
```
docker pull elgalu/selenium
docker pull dosel/zalenium

```
### Run Docker images
Linux
```
docker run --rm -ti --name zalenium -p 4444:4444 \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /tmp/videos:/home/seluser/videos \
      --privileged dosel/zalenium start 
```
OSX
```
docker run --rm -ti --name zalenium -p 4444:4444 \
      -e DOCKER=17.06.2-ce \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v /tmp/videos:/home/seluser/videos \
      --privileged dosel/zalenium start
```
Windows
```
docker run --rm -ti --name zalenium -p 4444:4444 ^
      -v /var/run/docker.sock:/var/run/docker.sock ^
      -v /c/Users/your_user_name/temp/videos:/home/seluser/videos ^
      --privileged dosel/zalenium start
```
