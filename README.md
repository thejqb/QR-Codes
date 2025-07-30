This is for Daniel Sun's Research project and is a piece of python code which can generate QR codes.

Files
gf.py - the pre-processing component. Turning the message, version, and ec level into the final bitstream, ready to be put into the QR code.
prepare-matrix.py - preparing all of the preset elements of the matrix - that is, finder, alignment, and timing patterns, as well as the dark module. This chunk also reserves places for the format and version information.
masking.py - inserts the final message created by gf.py into the qr code base created by prepare-matrix.py and does masking on it. Contains a penalty algorithm for determining the optimal mask pattern.
format-version-info.py - prepares and inserts the format and version information into their locations and displays the final QR code.
full.py - all four sections strung together, entirely functional and working.
