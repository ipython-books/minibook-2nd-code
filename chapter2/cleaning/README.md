NYC taxi dataset 2013
=====================

Instructions to create your own subset of the data:

* Clone this repository on your computer with `git clone https://github.com/ipython-books/minibook-2nd-code.git`

* Use a BitTorrent client (like http://www.utorrent.com/) to download the `nycTaxiFareData2013.torrent` and `nycTaxiTripData2013.torrent` datasets in `../data` (they have been obtained at http://chriswhong.com/open-data/foil_nyc_taxi/).

* Extract the two downloaded `tripData2013.zip` and `faredata2013.zip` files in the `/minibook-2nd-code/chapter2/data` directory.

* You now have 24 zip files named `trip_data_1.csv.zip`, ..., `trip_data_12.csv.zip`, `trip_fare_1.csv.zip`, ..., `trip_fare_12.csv.zip` in the `/minibook-2nd-code/chapter2/data` directory.

* Start a notebook server in the current directory (`minibook-2nd-code/chapter2/cleaning/`) with `jupyter notebook`, and open the `subset.ipynb` notebook.

* You can tweak the `step = 200` line at the top of the notebook. Use a lower value to get a larger subset. The proportion of the subset is `1/step` (so 0.5% with step = 200).

* Run this notebook. After several minutes, you will get two `trip_data_subset.csv` and `trip_fare_subset.csv` files in the data directory. These are the files we will be working on in this chapter and the next.
