
# Reproducible data analysis with make

An example on how to use `make` to structure data transformations in a declarative way.

The idea is to specify data transformations as `make` targets that modify the filename of an input file in a predictable way.
For example, a transformation called `step1` that modifies a `.csv` file is specified like this:

```make
build/%.step1.csv: build/%.csv step1.py
	python step1.py $< $@
```

In this case, the task is executed by a python script called `step1.py`.
In general, this could be anything that can be run from the shell.
The command line arguments that are passed to the script specify the input and output filenames.

After defining a few of these steps, we require `make` to run a certain sequence of steps by specifying the filename of the output we want:
```make
all: build/data.step1.step2.plot_everything.pdf
```

This would execute the tasks called `step1`, `step2`, and `plot_everything`.

See `Makefile` for a working example.

## Caveats

Although the workflow is usable, there are a few annoying problems:

- The script used for a task is not automatically checked by `make` for up-to-dateness, which means we have to specify it as a dependency for the target.
  This becomes annoying once we want to use several input files, because we then can't just pass the `make` variable with all dependencies to our script.
- `make` doesn't detect changes in the build commands themselves.
  This means `make` doesn't detect changes in arguments passed to the task.
  But this is a must if you want your tasks to be reusable.

