redis:
	docker run -d \
		-p 6380:6380 \
		--rm \
		--name=sentinel-redis \
		redis /bin/sh -c 'redis-server --appendonly yes --requirepass qwerty'


.PHONY: redis