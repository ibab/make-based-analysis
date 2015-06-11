
all: build/data.cut2.cut1.plot_x.pdf

build:
	mkdir -p build

build/data.csv: create_data.py | build
	python create_data.py $@

build/%.plot_x.pdf: build/%.csv plot_var.py
	python plot_var.py $< $@ "x"

build/%.cut2.csv: build/%.csv cut.py
	python cut.py $< $@ "x > 1"

build/%.cut1.csv: build/%.csv cut.py
	python cut.py $< $@ "y < 0"

clean:
	rm -r build

.SECONDARY:

