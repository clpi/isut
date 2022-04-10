# This is just an example to get you started. Users of your library will
# import this file by writing ``import inm/submodule``. Feel free to rename or
# remove this file altogether. You may create additional modules alongside
# this file as required.
import nimpy

type DemoModel* = ref object of PyNimObjectExperimental
  id*: string
  steplen*: int
  sectlen*: int
  name*: string
  created*: string
  sects: seq[string]

# proc initDemo*(demo: DemoModel): DemoModel {.exportpy.} =
#   echo "initializing demo"


type
  Demo* = object
    name*: string