# ddjt_logging

Minimal reproducer app and instructions for https://github.com/jazzband/django-debug-toolbar/pull/1603

## Set up and test logging without DDT

### Pre-requisites

Assume you've cloned this repo into some folder `$src/ddjt_logging`  
In the next steps you will install [DDT](https://github.com/riwatt/django-debug-toolbar) into a sibling folder `$src/django-debug-toolbar-dev`. 

### Create / Activate the virtualenv of your choice
This example uses pyenv-virtualenv:

```sh
$ pyenv virtualenv 3.9.11 ddjt_logging
$ pyenv local ddjt_logging
```

### Install Django

```sh
$ pip install Django==4.0.3
```

### Start dev server

```sh
# first time init
$ ./manage.py migrate
$ ./manage.py runserver
```

### Observe that logging goes to stderr

Visit http://127.0.0.1:8000/ 

You will see a timestamp in your browser:

![image](https://user-images.githubusercontent.com/646354/161497763-79e849c8-dc13-4e9b-b2f8-da5aab823f67.png)

And corresponding loglines in your server's console:

![image](https://user-images.githubusercontent.com/646354/161497884-5afe188b-6757-4e2c-99a8-b47e2e7eaf73.png)

## Set up and test logging with mainline DDT

### Install editable dev version of DDT

Outside this repo but inside this virtualenv.

```sh
$ cd ..
$ git clone https://github.com/riwatt/django-debug-toolbar.git django-debug-toolbar-dev
$ cd django-debug-toolbar-dev
# this will check out a commit before the logging fix
$ git checkout 54e63f0494414ae0d93abc6e202d5f644c75952a
# make sure we're installing into the right virtualenv
$ pyenv shell ddjt_logging
$ pip install -e . 
```
### Configure DDT for this app

```sh
# assuming you're still in the ddt-dev directory
$ cd ../ddjt_logging
$ git checkout debug-toolbar-default-install
```

### Observe that logging is now swallowed by DDT's logging panel

With the devserver still running go to http://127.0.0.1:8000/ again and see that logging is now intercepted by DDT:

<img width="868" alt="image" src="https://user-images.githubusercontent.com/646354/161496113-be826fec-f9ff-4695-ab04-05cb77c6dd88.png">

<img width="868" alt="image" src="https://user-images.githubusercontent.com/646354/161496504-e77a922e-5b64-4b53-b7a0-c79e7355c5d6.png">

But the stderr logs are gone:

<img width="842" alt="image" src="https://user-images.githubusercontent.com/646354/161496271-49d4859b-2574-4825-a1cc-f269d3844ade.png">


## Confirm logging with patched DDT

### Check out the patch

In the ddt directory:

```sh
git checkout 945bd92ec7a7b012d3e80ced2403b38d2feaa8b9
```

### Confirm the patch works

Make sure the django server is still running and go to http://127.0.0.1:8000/ confirm that we have logs again in stderr (as well as in DDT):

<img width="868" alt="image" src="https://user-images.githubusercontent.com/646354/161497487-7fb3e68c-146e-4b57-a1bd-b0cc49ee2ab8.png">

<img width="868" alt="image" src="https://user-images.githubusercontent.com/646354/161497501-68cdfa16-3c40-4750-bfed-0494042bd617.png">

<img width="842" alt="image" src="https://user-images.githubusercontent.com/646354/161497524-a8bfd238-5992-4d97-b947-183cf5497562.png">

## Some more config examples

Find more config settings knobs to turn in the `with-examples` branch.  

