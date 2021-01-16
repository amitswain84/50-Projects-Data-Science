from altair.vegalite.v4.api import sequence
import pandas as pd
import streamlit as st
# Altair is a declarative statistical visualization library for Python. With Altair, you can spend more time understanding your data and its meaning.
# More at https://pypi.org/project/altair/
import altair as alt
from PIL import Image


st.write("""
# DNA Nucleotide Count Web App

This APP Counts the Nucleotide Composition of Query DNA!

***
""")


st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 1\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=220)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skip the First Line as its the Name of Input Area
sequence = ''.join(sequence)

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')
# 1. Print dictionary
st.subheader('1. Print dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d


X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

# 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' Adenine (A)')
st.write('There are  ' + str(X['T']) + ' Thymine (T)')
st.write('There are  ' + str(X['G']) + ' Guanine (G)')
st.write('There are  ' + str(X['C']) + ' Cytosine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(50)
)
st.write(p)
