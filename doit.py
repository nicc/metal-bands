from textgenrnn import textgenrnn

# -- to retrain new models:
# textgenBands = textgenrnn().train_from_file('data/black-metal-bands.txt', num_epochs=1)
# textgenBandAbstracts = textgenrnn().train_from_file('data/black-metal-band-abstracts.txt', num_epochs=1)
# textgenAlbums = textgenrnn().train_from_file('data/black-metal-albums.txt', num_epochs=1)
# textgenAlbumAbstracts = textgenrnn().train_from_file('data/black-metal-album-abstracts.txt', num_epochs=1)
# -- 


# -- to reuse existing models:
textgenBands = textgenrnn('models/black-metal-bands-model.hdf5')
textgenBandAbstracts = textgenrnn('models/black-metal-band-abstracts-model.hdf5')
textgenAlbums = textgenrnn('models/black-metal-albums-model.hdf5')
textgenAlbumAbstracts = textgenrnn('models/black-metal-album-abstracts-model.hdf5')
# -- 

# -- to generate predictions:
# - first arg says how many predictions to make
# - a higher temperature will make the results more "creative"
print("\n\n\n-- BANDS: --\n\n") 
textgenBands.generate(30, temperature=0.75)
print("\n\n\n-- BAND ABSTRACTS: --\n\n") 
textgenBandAbstracts.generate(10, temperature=0.5)
print("\n\n\n-- ALBUMS: --\n\n") 
textgenAlbums.generate(30, temperature=0.65)
print("\n\n\n-- ALBUM ABSTRACTS: --\n\n") 
textgenAlbumAbstracts.generate(10, temperature=0.5)