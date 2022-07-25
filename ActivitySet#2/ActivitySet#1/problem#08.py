"""Write code using find() and string slicing  to extract the number at the end of the line below."""
text = "X-DSPAM-Confidence:    0.8475";
startPos = text.find(' ')
piece = text[startPos+1:]
end = float(piece)
print(end)