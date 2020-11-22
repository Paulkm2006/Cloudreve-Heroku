FROM centos:latest
WORKDIR /root/cloudreve
ADD cloudreve ./cloudreve
ADD conf.ini ./conf.ini
ADD run.sh ./run.sh
RUN yum update -y && yum install glibc-utils glibc-devel glibc-headers epel* wget curl nano python3 -y && chmod +x ./cloudreve && chmod +x ./run.sh
CMD ./run.sh
