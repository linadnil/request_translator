default:
	@echo "'make install[2]' for installation"
	@echo "'make check[2]' for tests"

install:
	python ./setup.py install

install2:
	python2 ./setup.py install

check:
	nosetests -v -d --cover-erase --with-coverage --cover-package=hrt

check2:
	nosetests2 -v -d --cover-erase --with-coverage --cover-package=hrt
