use clang_format::ClangFormatStyle;
use cxx_qt_build::CxxQtBuilder;

fn main() {
    CxxQtBuilder::new()
        .cpp_format(ClangFormatStyle::Mozilla)
        .file("src/lib.rs")
        .build();
}