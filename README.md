This is just a little script that lists all of your files inside of inside a directory to a single ```.txt``` file, which is the most efficient way I've seen of giving context to an LLM, skipping attachment file limits.

# How to use it
```
python3 context.py <folder_dir> <optional_params>
```

# Parameters
- ```-skip_dir```  => Skips specified individual subdirectories separated by commas
- ```-skip_file``` => Skips specified individual files separated by commas
- ```-skip_dot```  => Skips all files starting with "." except envs (since this is contextual, can be changed)

This will give you an ```output_context.txt``` file in the same place ```context.py``` is located.

I personally use this command ( for react apps) :
```python3 context.py klip/ -skip_dir temp,node_modules,.git,.next -skip_file favicon.ico,package-lock.json -skip_dot```

Note: You can skip folders you don't want to list as well
