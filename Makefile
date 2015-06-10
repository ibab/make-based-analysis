
all: build/test.txt build/data.cut2.cut1.root

build:
	mkdir -p build

build/data.root: create_data.py | build
	python create_data.py $@

build/%.plot_x.pdf: build/%.root plot_var.py
	python plot_var.py $< $@ "x"

build/%.cut2.root: build/%.root cut.py
	python cut.py $< $@ "x > 1"

build/%.cut1.root: build/%.root cut.py
	python cut.py $< $@ "y < 0"

build/test.txt: cpp-template/build/bin/default | build
	sleep 1
	echo 1
	sleep 1
	echo 2
	sleep 1
	echo 3
	cpp-template/build/bin/default > $@

#build/%.root: %.root | build
#	cp $< $@

clean:
	rm -r build

cpp-template/build/bin/default:
	cd cpp-template/build/ && cmake .. && make

.SECONDARY:

