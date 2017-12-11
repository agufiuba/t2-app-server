# Para ejecutar estos tests en docker:
# docker-compose exec -ti t2appserver_app-server_1 sh /as/src/test.sh
export PYTHONPATH=$PYTHONPATH:$(pwd)/src/llevame
pytest
