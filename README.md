# whoami
 Simple Flask application for my website - https://eduardgro.su/whoami
 
## Environment
- Python 3.8.10
- nginx 1.18.0 (Ubuntu)

## Installation
nginx/sites-available/eduardgro.su
```
server {
    ...

    root /var/www/eduardgro.su;
    index index.html index.php;
    ...
 
    location /whoami {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:8080;
    }
}
```

## Notes
- Do not use this in production. See [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/).
- I am not going to post installation step by step. You need to have a basic understanding of how to use nginx.
