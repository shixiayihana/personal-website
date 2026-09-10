#!/usr/bin/env bash
set -Eeuo pipefail

cd /www/wwwroot/www.11251236.xyz/personal-website
git pull --ff-only

cd frontend
npm run build