from textgenrnn import textgenrnn

# -- to create new model:
# textgen = textgenrnn()
# textgen.train_from_file('data/bands.txt', num_epochs=1)
# -- 

# -- to reuse existing model"
textgen = textgenrnn('data/model.hdf5')
# -- 

# first arg says how many predictions to make
# a higher temperature will make the results more "creative"
textgen.generate(30, temperature=0.75)