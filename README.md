# plot
This is a command line package for using matplotlib
to make plots based on input JSON or YAML file.

## Examples
This package is still in active development.  
For examples, you can take a look at the [test/run](https://github.com/yuhangwang/plot/tree/master/test/run) folder.
Currently `plot` supports plotting `line`, `bar`, `matrix` and `span` plots.
The full list of available parameters can be found in the [plot/parameter](https://github.com/yuhangwang/plot/tree/master/plot/parameter) folder.  
In the subfolders: `data`, `global` and `local`,
the `all.yaml` contains all the parameters for each these fields.
It is automatically generated using the the individual yaml files,  
such as `bar.yaml`, `line.yaml`, etc.
A documentation will be available soon.


## Support for MacOS
To avoid TK crashing problem on MacOS, do the followings
(see https://github.com/MTG/sms-tools/issues/36#issuecomment-296493101)
```bash
mkdir -p ~/.matplotlib`
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc`
```

## License
MIT/X11 (c) Yuhang(Steven) Wang, 2016