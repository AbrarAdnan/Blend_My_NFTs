# config.py is where you can configure the settings of your NFT collection

nftName = ''  # The name of the NFT image produces by PNG-Generator
imageFileFormat = ''  # Dictate the image extension when Blender renders the images
# Type the exact name provided below in the '' above:
# JPEG - Exports the .jpeg format
# PNG - Exports the .png format
# Visit https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image.file_format
# for a complete list of file formats supported by Blender. Enter the file extension exactly as specified in
# the Blender API documentation.

# The path to Blend_My_NFTs folder:
save_path_mac = '/Users/Path/To/Blend_My_NFTs'
save_path_windows = r''
# Place the path in the '', e.g: save_path_mac = '/Users/Path/to/Blend_My_NFTs'
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs

maxNFTs = 10  # The maximum number of NFTs you want to generate.
nftsPerBatch = 10  # Number of NFTs per batch
renderBatch = 1  # The batch number to render in Exporter.py

# Set to True to generate images or 3D models depending on your settings below when main.py is run in Blender.
# Only works if you have already generated NFTRecord.json and all batches.
renderImage = False

### Select colour or material.###
# Object generation options:
enableGeneration = False  # When set to true this applies the sets of colors listed below to the objects in the collections named below

generationType = 'material'  # You can either set 'color' or 'material' here. Type you set will correspond to following options.
# generationType = 'material' mode is experimental. Be sure that you back-up your file.
# You need to set materials as "fake user". Do not miss this step. Or your materials going to vanish after running this script.

# The collections below are RGBA Color values. You can put as many or as little color values in these lists as you would like.
# You can create any number of rgbaColorLists and assign them to any number of collections that you would like.
# Each set of rgbaColorList1 assigned to an object by collection name in the colorList will act like an attribute and create a unique variant of that item.
rgbaColorList1 = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 1, 1), (.5, 0, 0, 1)]
rgbaColorList2 = [(1, 1, 0, 1), (0, 1, 1, 1), (.5, 0, 1, 1), (.5, 1, 1, 1), (0, .5, 0, 1)]
# The following color list can be as long or as short as you want it to be.
# To use this all you need to do is place the name of the collection you want colored in the "" and the set of colors you want to apply to it after the :
# The collection named can only contain objects and not sub collections. Every object in the collection will be set to the colors you assigned above for each attribute
if generationType == 'color':  # Do not change this line.
    colorList = {"Cube_1_33": rgbaColorList1, "Sphere_4_0": rgbaColorList2}

### These materials must be in your Current Files' Materials. Make sure that you've set your materials as "fake user". ###
# The collections below are Current Files' Materials. You can put as many or as little materials values in these lists as you would like.
# You can create any number of materialLists and assign them to any number of collections that you would like.
# Each set of materialLists assigned to an object by collection name in the materialList will act like an attribute and create a unique variant of that item.
materialList1 = ['Material1', 'Material1.001', 'Material1.002', 'Material1.003', 'Material1.004']
materialList2 = ['Material2', 'Material2.001', 'Material2.002', 'Material2.003', 'Material2.004']

# The following material list can be as long or as short as you want it to be.
# To use this all you need to do is place the name of the collection you want materials assigned in the "" and the set of materials you want to apply to it after the :
# The collection named can only contain objects and not sub collections. Every object in the collection will be set to the materials you assigned above for each attribute
if generationType == 'material':  # Do not change this line.
    colorList = {"Cube_1_33": materialList1, "Sphere_2_0": materialList2}

# 3D model imports and exports variables:
enable3DModels = False  # Set to True if using external models as attributes instead of Blender objects
# ^Does not work with colour options and rarity, both must be turned off in order to use this.

objectFormatExport = ''  # The file format of the objects you would like to export
# The following are file formats Blender accepts for exporting object files.
# Please type the exact name provided below in the '' above:
# fbx - The .FBX file format
# glb - The .glb file format
# obj - The .obj file format *Exports both a .obj and a .mtl files for the same generated object
# x3d - The .x3d file format

# Meta Data generation
enableMeteData = True  # Set to True to turn on meta data, set to False to turn off meta data generation.

metaDataType = 'DEFAULT'  # Select the format of the generated Meta Data for your NFTs blockchain.
# DEFAULT - The default setting; exports variants, dna, number, name, and rarity of each NFT to a dictionary (Not a blockchain standard)
# ADA - Cardano - Format Source: https://cips.cardano.org/cips/cip25/
# SOL - Solana - Format Source: https://docs.metaplex.com/nft-standard
# ERC721 - Ethereum ERC721 - Format Source: https://eips.ethereum.org/EIPS/eip-721

# NOTE: This is just the information Blend_My_NFTs can provide, you will have to add policy ID, URI information, etc
# yourself when you upload and mint your NFT collection.
# DISCLAIMER: These are only templates based on the common standards for the given blockchain, you will have to modify
# and fill them in with a script of your own when you mint your NFT collection. These metadata templates are only provided
# for your convenience.

metaDataDescription = ''  # The description of your NFT that will be inserted into its meta data

enableResetViewport = True  # If True: turns all viewport and render cameras on after Image_Generator is finished operations

# Utilities - DO NOT TOUCH:
import platform

mac = 'Darwin'
windows = 'Windows'
slash = ''
save_path = None

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = save_path_mac
    slash = '/'
elif platform.system() == windows:
    save_path = save_path_windows
    slash = '\\'

# Paths to folders
batch_save_path = save_path + slash + 'Batch_Json_files'  # The output path for batches generated by Batch_Sorter.py
images_save_path = save_path + slash + 'NFT_Image_Output'  # The output path for images generated by Exporter.py
modelAssetPath = save_path + slash + "3D_Model_Input"  # The input path for 3D models
model_save_path = save_path + slash + "3D_Model_Output"  # The output path for 3D models generated by Model_Generator.py
model_Script_Ignore_Path = modelAssetPath + slash + "Script_Ignore_Folder"  # The path to the Script_Ignore_Folder for 3D models

# error handling #

if objectFormatExport not in ['fbx', 'glb', 'obj', 'x3d'] and enable3DModels:
    raise ValueError("Output format in `objectFormatExport` can only be 'fbx', 'glb', 'obj', 'x3d'.")

# EXPERIMENTAL FEATURES:

# Enables Rarity_Sorter to weigh NFT DNA attributes and variants:
enableRarity = False
# generateColors must be turned off and enableMaxNFTs must be turned on.
# True = include weighted rarity percentages in NFTRecord.json calculations,
# False = Pure random selection of variants

# Preview and render test settings:
# Set to True to run Preview test, set to False to stop test. Run main.py in Blender to initiate the test.
# enable3DModels must be off to run the render test.
runPreview = False
maxNFTsTest = 5  # Increase to get a more accurate reading of the render time. The number of images generated in the render test.

# Turn this on when you run main.py to generate NFTRecord.json and appropriate batches to confirm there are no duplicate
# NFT DNA.
checkDups = False