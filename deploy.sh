#!/usr/bin/env bash
set -Eeuo pipefail

cd /www/wwwroot/www.11251236.xyz/personal-website
git pull https://gitee.com/tangwenlin/personal-website.git main --ff-only

cd frontend
npm run build