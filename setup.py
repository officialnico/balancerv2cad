import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='balancerV2_Model',  
     version='1.0',
     scripts=['StableMath, StablePool, WeightedMath, WeightedPool'] ,
     author="Nico Rodriguez, Thomas Liu, Marcin Jaczynski",
     author_email="metavisionlabs@protonmail.com",
     description="Balancer V2 files",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/officialnico/balancerV2_Model.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
