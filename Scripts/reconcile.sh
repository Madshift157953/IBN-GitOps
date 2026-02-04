#!/bin/bash
set -e

cd /root/ibn-gitops/IBN-GitOps

git pull origin main
sudo python3 controller/apply_intent.py
