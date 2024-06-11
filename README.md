# crawler
A selenium based crawler util
Supabase db with text search

Setup Standalone

sudo python3 -m flask run --host=0.0.0.0  

Setup Docker

sudo docker build -f Dockerfile.dev -t crawler:1.0.0 .
sudo docker run -p 5000:5000 crawler:1.0.0
