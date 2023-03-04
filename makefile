install:
	python -m pip install -Ue .[dev,pretty]

.venv:
	python -m venv .venv
	source .venv/bin/activate && make install
	echo 'run `source .venv/bin/activate` to activate virtualenv'

venv: .venv

test:
	python -m unittest -v plinky
	python -m mypy -m plinky

lint:
	python -m flake8 plinky
	python -m ufmt check plinky

format:
	python -m ufmt format plinky

release: lint test clean
	flit publish

clean:
	rm -rf .mypy_cache build dist html *.egg-info

distclean: clean
	rm -rf .venv
