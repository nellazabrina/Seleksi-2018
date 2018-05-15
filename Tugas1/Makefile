all: clean build run

clean: # remove data and binary folder
sudo rm -f bali.json
sudo rm -f "di yogyakarta.json"
sudo rm -f "dki jakarta.json"
sudo rm -f "kota bandung.json"
sudo rm -f "kota malang.json"
sudo rm -f "kota surabaya.json"

build: # compile to binary (if you use interpreter, then do not implement it)
python3 -m py_compile scrapper.py

run: # run your binary
python3 src/scraper.py
