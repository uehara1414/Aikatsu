# Aikatsu
アイデア創出活動支援プラットフォーム

## Requirements
- pipenv
- polymer-cli
- bower

## Install

```sh
git clone git@github.com:uehara1414/Aikatsu.git
cd Aikatsu
pipenv install
pipenv run python manage.py migrate
cd aikatsu/static
bower install
polymer build
cd ../..
pipenv run python manage.py runserver 8000
```

and open http://127.0.0.1:8000/
