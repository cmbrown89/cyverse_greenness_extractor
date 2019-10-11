FROM agdrone/cyverse_base_extractor_plot:1.0
LABEL maintainer="Clairessa Brown <clairessabrown@email.arizona.edu>"

# Run upon docker startup
COPY extractor.py /home/extractor/
RUN chmod +x /home/extractor/extractor.py

# Define entry point
WORKDIR /home/extractor/
ENTRYPOINT ["/home/extractor/extractor.py"]

# Model command arguments after tester.py script
# Have extractor accept image file(s) and optional output file name
# Have extractor return list of greenness indices 
CMD ["",""]
