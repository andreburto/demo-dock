# Docker-compose + Nginx + Uwsgi + Flask

## About

This project is a small demo that combines Docker, Nginx, uWsgi, and Flask to run a little web site that shows pictures.
The pictures are stored in a WordPress MySQL database, so if you want to use thus project you'll need one of those too.

Please don't use this project. 
It's just a toy for me to test out ideas on without having to start from scratch every time.

## Setup

1. Clone this project locally.
2. Update the `.env.example` file and rename it to `.env`.
   1. DATABASE, DBHOST, DBUSER, and DBPASS refer to the MySQL to which you wish to connect.
   2. SEARCH_TERM is the WordPress tag slug that corresponds to the image you want to display.
3. Run `docker-comppose build`.
4. Run `docker-compose up`.
5. Visit http://localhost/.
