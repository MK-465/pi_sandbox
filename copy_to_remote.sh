#!/bin/bash
ssh pi@192.168.100.15 'rm -rf ~/projects/grove_sandbox/pi_sandbox/src/'
#ssh pi@192.168.100.15 'rm -rf ~/projects/grove_sandbox/pi_sandbox/resources/'
ssh pi@192.168.100.15 'rm ~/projects/grove_sandbox/pi_sandbox/requirements.txt'
scp -r ./src/ pi@192.168.100.15:~/projects/grove_sandbox/pi_sandbox/
#scp -r ./resources/ pi@192.168.100.15:~/projects/grove_sandbox/pi_sandbox/
scp -r ./requirements.txt pi@192.168.100.15:~/projects/grove_sandbox/pi_sandbox/requirements.txt
ssh pi@192.168.100.15 'pip3 install -r ~/projects/grove_sandbox/pi_sandbox/requirements.txt'

