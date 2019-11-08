* Clone this project:
``` bash
git clone
```
* change directory to this project:
``` bash
cd shanshuiDadA_pth
```
* Install anaconda through [official instruction](https://www.anaconda.com/download/) or if you on mac, you can just run (might need to reboot afterwards)
``` bash
bash Anaconda3-5.3.0-MacOSX-x86_64.sh
```
* Install [Node](https://nodejs.org/en/download/package-manager/)
* Create conda environment from the **environment.yml** file:
(This will automatically install all necessary dependencies, so it might take a while depends on your setup)
``` bash
conda env create -f environment.yml
```
* Activate conda environment:
``` bash
source activate shanshuiDaDA_pth
```
* Start node.js server
``` bash
node newapp.js
```
* Open [localhost:5000](http://localhost:5000/) in your browser
* OR (Suggested!) Use ** a touch screen device eg.Tablet, Smart Phone etc.** to load the url and draw SHANSHUI from there. If you don't know how to, refer to this [instruction]().

If you find the code useful for your research, please cite our paper:

    @inproceedings{PremiLab,
      title={An Interactive and Generative Approach for Chinese Shanshui Painting Document},
      author={Le Zhou, Qiu-Feng Wang, Cheng-Hung Lo, Kaizhu Huang},
      booktitle={The International Conference on Document Analysis and Recognition (ICDAR)},
      year={2019}
    }