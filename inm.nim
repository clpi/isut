import nimpy
import sugar, algorithm, tables, sequtils, strformat
import pixie, options
import arraymancer

import inm/demo, inm/draw

# proc readImg*(f: File): Image {.exportpy.} =
#   var res: Image = newImage(1920, 1080)
#   var dups = initTable[string, int]()
#   return res

proc dtype*(ty: PyObject): PyObject =
  nimpy.getAttr(ty, "dtype")

proc pyprint*(o: PyObject): void =
  let py = pyBuiltinsModule()
  discard nimpy.callMethod(py, "print", [o])

type Step* = object
  title: string
  dir: string
  audio: string
  image, hover: string
  x, y: int
  hiX, hiY: int
  animated: bool
  hasMouse: bool

type Section* = object
  title: string
  dir: string
  audio: string
  steps: seq[Step]

type Demo* = object
  title: string
  dir: string
  path: string
  sections: seq[Section]


proc add(x: int, y: int): int {.exportpy.} =
  ## Adds two files together.
  return x + y
