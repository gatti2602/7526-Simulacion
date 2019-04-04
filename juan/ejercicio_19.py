import scipy.stats as st


obs_values = [25,8,17,20,13,13]
f_values = [16,16,16,16,16,16]
(a,p) = st.chisquare(obs_values, f_exp=f_values)
#print a
# si p es < que alfa (0,05) entonces lo podes descartar 
print 1-p
print 1-p<0.05