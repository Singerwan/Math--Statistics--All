import streamlit as st
from streamlit_markdown import st_markdown


st.title("Pascal's Triangle Ms.Stanton")

markdown_text1 = "$ \\huge \\boxed{^nC_r = ^{n-1}C_{r-1} + ^{n-1}C_r}$"
markdown_text2 = """$ \\overbrace
{\\text{10 pizza
choosing 3 toppings}}^{\\textcolor{blue}
{\\boxed{
    \\Large (^{10}C_3)}}}  ,  <> 
  \\underbrace{\\text{  VS  if anchovies are not 
allowed or allowed, 
how many different pizzas can be made?}}_{
    \\boxed{
    \\textcolor{red}{\\Large
   ^{n(10)-1=9}C_{r(3)-1=2} + ^{9}C_2 }}}$"""
markdown_text3 = """$\\Large 
\\frac{(n-1)!}{  ( \\textcolor{brown}{(n-1)}- \\textcolor{magenta}{(r-1) )}! ( r-1 )!)}
+
\\frac{(n-1)!}{(n-1-r)!(r)!}
$"""
markdown_text4 = """$\\Large
\\frac{(n-1)}{(n-r)!(r-1)!}
+\\frac{(n-1)!}{(n-1-r)!(r)!}$"""

markdown_text5 = """$\\Large
\\frac{(n-1)}{(n-r)!(r-1)!}
+\\frac{(n-1)!}{(n-r-1)!(r)!}$"""


markdown_text6 = """$\\Large
\\frac{(n-1)}{(n-r)
\\textcolor{blue}{\\boxed{(n-r-1)!}}
\\textcolor{brown}{\\boxed{(r-1)!}}}
+\\frac{(n-1)!}{
\\textcolor{blue}{\\boxed{(n-r-1)!}}
    (r)
\\textcolor{brown}{\\boxed{(r-1)!}}}$"""

markdown_text7 = """$\\Large
\\frac{r(n-1)!+(n-r)(n-1)!}{r(n-r)
\\textcolor{blue}{\\boxed{(n-r-1)!}}
\\textcolor{brown}{\\boxed{(r-1)!}}}
$"""

markdown_text8 = """$\\Large
\\frac{(n-1)!(\\cancel{r} + n- \\cancel{r})(n-1)!}{r(n-r)
\\textcolor{blue}{\\boxed{(n-r-1)!}}
\\textcolor{brown}{\\boxed{(r-1)!}}}$"""

markdown_text9 = """$\\Large
\\frac{n!}{r!(n-r)!}$"""

st_markdown(markdown_text1)
st_markdown(markdown_text2)
st_markdown(markdown_text3)
st_markdown(markdown_text4)
st_markdown(markdown_text5)
st_markdown(markdown_text6)
st_markdown(markdown_text7)
st_markdown(markdown_text8)
st_markdown(markdown_text9)
st.markdown(":yellow-background[:red[Right-Hand-Side=Left-Hand-Side]]")

st.title("Binomial -Coin-Toss ")
st.subheader("2 Coin Tosses")
st.subheader("HH | TT | HT | TH ")
markdown_text10="""
$\\Large
(\\textcolor{blue}{
    \\overbrace{
        \\frac{1}{2}}
        ^{\\text{H}}}
+\\textcolor{red}{
    \\underbrace{
        \\frac{1}{2}}_
        {\\text{T}}})^2=
(\\textcolor{blue}{\\overbrace{
    \\frac{1}{2})^2}^{
        \\text{HH}}}+
        \\underbrace{
        \\textcolor{black}{
\\boxed{2}}
(\\frac{1}{2})
(\\frac{1}{2})}_{\\text{2 ways (HT or TH)}}
+(\\textcolor{red}{\\overbrace{
    \\frac{1}{2})^2}^{
        \\text{TT}}}
$"""
st.subheader("3 Coin Tosses")
st.subheader("HHH | TTT | HHT | HTH | THH | TTH | THT | HTT")
st_markdown(markdown_text10)

markdown_text11="""
$\\Large
(\\textcolor{blue}{
    \\overbrace{
        \\frac{1}{2}}
        ^{\\text{H}}}
+\\textcolor{red}{
    \\underbrace{
        \\frac{1}{2}}_
        {\\text{T}}})^3=
(\\textcolor{blue}{\\overbrace{
    \\frac{1}{2})^3}^{
        \\text{HHH}}}+
        \\underbrace{
        \\textcolor{black}{
\\boxed{3}}
(\\frac{1}{2})^2
(\\frac{1}{2})^1}_{
    \\text{3(
        HHT|THH|HTH)}}+
\\underbrace{\\boxed{3}(\\frac{1}{2})^1
(\\frac{1}{2})^2}_{
    \\text{3(TTH|THT|HTT)}}
+(\\textcolor{red}{\\overbrace{
    \\frac{1}{2})^3}^{
        \\text{TTT}}}
$"""
st_markdown(markdown_text11)