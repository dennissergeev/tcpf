#!/usr/bin/env bash

echo $PWD

export FORTRAN=gfortran
export EXECUTABLE=model.x

# Set netCDF paths
NETCDF_LIB=`nc-config --flibs`
NETCDF_INC=`nc-config --fflags`
if [[ $FORTRAN == "gfortran" ]]; then
  NETCDF_INC=-I$NETCDF_INC
  NETCDF_LIB="$NETCDF_LIB -lnetcdff -lnetcdf"
fi
echo $NETCDF_INC
echo $NETCDF_LIB
export NETCDF_INC
export NETCDF_LIB

make $EXECUTABLE
if [ $? != 0 ]; then
    echo "ERROR: make failed for $EXECUTABLE"
    exit 1
fi
