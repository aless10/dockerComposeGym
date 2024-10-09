# dockerComposeGym

This repo is a collection of things that I learnt about the usage of docker compose.

## Override

Docker compose lets you have multiple compose files and execute them together. This feature lets you also override services configuration.
This is particularly helpful when you have a base docker compose and you have the ``dev`` compose and the `prod` one.
This can be achieved by using the ``-f`` flag. The documentation for this feature can be found [here](https://docs.docker.com/compose/how-tos/multiple-compose-files/)

One of the thing that I did not know at first (but it is documented in the official docker compose doc) is that by default docker compose tries to run 
the ``docker-compose.yml`` and the `docker-compose.override.yml`. So if you have both these files and you run `docker compose up`, they are automatically 
executed.

You can try it by going in the ``override`` directory and run `docker compose up`. You can see that the value displayed is the one set in the `docker-compose.override.yml` file.

```shell
cd override
docker compose up
```

## Compose filename

Docker compose lets you have multiple compose files. But what is the hierarchy of the filenames that is going to look at by default?
Well at first I would say that ``docker-compose.yml`` is the preferred one. Actually, this award goes to `compose.yml`.

You can read this in the documentation [here](https://docs.docker.com/compose/intro/compose-application-model/#the-compose-file)
You can try it by going in the ``compose_filename`` directory and run `docker compose up`. You can see that the value displayed is the one set in the `compose.yml` file.

```shell
cd compose_filename
docker compose up
```