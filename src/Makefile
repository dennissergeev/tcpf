EXECUTABLE = model.x
OBJ = atmos.o base.o
INCS = $(NETCDF_INC)
LIBS = $(NETCDF_LIB)

all: $(EXECUTABLE)

%.o: %.f90
	$(FORTRAN) -c $(INCS) $^

$(EXECUTABLE): $(OBJ)
	$(FORTRAN) -o $@ $(OBJ) $(INCS) $(LIBS)

clean:
	-rm -f $(OBJ) $(EXECUTABLE)
