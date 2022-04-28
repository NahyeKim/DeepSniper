
# DeepSniper

Predicting on/off-target effects of Sniper gene editor


## System Requirements



```bash
    Python   3.7.7
    Python Packages:
    numpy 1.19.5
    pandas 1.3.0

    Tensorflow and dependencies:
    Tensorflow  2.5
    CUDA       11.2.0
    cuDNN       8.1.0
```
    
## Demo Instructions (required time, <1 min)

#### (1) Sniper1.0 on-target

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp), feature		
    GGATGACTACGCCTCTGCCTTagtAGGTCA, 1
```
+ Input2: `./Sniper_on_1_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
    target + PAM	feature	Prediction score
    GGATGACTACGCCTCTGCCTTagtAGGTCA	1	47.06348038
```
+ Run script:
```
    python ./Sniper_on_1.py
```

#### (2) Sniper2.0L on-target

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp), feature		
    GGATGACTACGCCTCTGCCTTagtAGGTCA, 1
```
+ Input2: `./Sniper_on_2_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
    target + PAM	feature	Prediction score
    GGATGACTACGCCTCTGCCTTagtAGGTCA	1	54.93514633
```
+ Run script:
```
    python ./Sniper_on_2.py
```

#### (3) Sniper1.0 off-target Day4

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Guide (X20),Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp)		
    GACTACGCCTCTGCCTTTCA,GGATGACTACGCCTCTGCCTTagtAGGTCA
```
+ Input2: `./Sniper_off_1_4_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
Output: ./prediction_result.xlsx
    Guide (X20)	target + PAM	Prediction score
    GACTACGCCTCTGCCTTTCA	GGATGACTACGCCTCTGCCTTagtAGGTCA	-0.06326002628
```
+ Run script:
```
    python ./Sniper_off_1_4.py
```

#### (4) Sniper2.0L off-target Day4

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Guide (X20),Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp)		
    GACTACGCCTCTGCCTTTCA,GGATGACTACGCCTCTGCCTTagtAGGTCA
```
+ Input2: `./Sniper_off_2_4_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
Output: ./prediction_result.xlsx
    Guide (X20)	target + PAM	Prediction score
    GACTACGCCTCTGCCTTTCA	GGATGACTACGCCTCTGCCTTagtAGGTCA	-0.08977238834
```
+ Run script:
```
    python ./Sniper_off_2_4.py
```

#### (5) Sniper1.0 off-target Day7

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Guide (X20),Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp)		
    GACTACGCCTCTGCCTTTCA,GGATGACTACGCCTCTGCCTTagtAGGTCA
```
+ Input2: `./Sniper_off_1_7_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
Output: ./prediction_result.xlsx
    Guide (X20)	target + PAM	Prediction score
    GACTACGCCTCTGCCTTTCA	GGATGACTACGCCTCTGCCTTagtAGGTCA	0.01810191758
```
+ Run script:
```
    python ./Sniper_off_1_7.py
```

#### (3) Sniper2.0 off-target Day7

+ Input1: `./input_example.csv`  # List of Target Sequence(s)
    + File format:
```
    Guide (X20),Target number	30 bp target sequence (4 bp + 20 bp protospacer + PAM + 3 bp)		
    GACTACGCCTCTGCCTTTCA,GGATGACTACGCCTCTGCCTTagtAGGTCA
```
+ Input2: `./Sniper_off_2_7_model/` # Pre-trained Model Files

+ Output: ./prediction_result.xlsx
```
Output: ./prediction_result.xlsx
    Guide (X20)	target + PAM	Prediction score
    GACTACGCCTCTGCCTTTCA	GGATGACTACGCCTCTGCCTTagtAGGTCA	-0.09411415458
```
+ Run script:
```
    python ./Sniper_off_2_7.py
```