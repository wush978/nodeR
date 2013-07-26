{
  "targets": [
    {
      "target_name": "helloR",
      "sources": [ "helloR.cpp" ],
      "include_dirs": [ 
        '<!@(Rscript -e "retval <- system(\'R CMD config --cppflags\', intern=TRUE);cat(substr(retval, 3, nchar(retval)))")',
        '<!@(Rscript -e "cat(system.file(\'include\', package=\'RInside\'))")',
        '<!@(Rscript -e "cat(system.file(\'include\', package=\'Rcpp\'))")',
      ],
      'cflags!': ['-fno-exceptions', '-fno-rtti'],
      'cflags_cc!': ['-fno-exceptions', '-fno-rtti'],
      "link_settings": {
        "libraries": ['<!@(Rscript -e "RInside:::LdFlags()")', '<!@(Rscript -e "Rcpp:::LdFlags()")', '-lR'],
        "library_dirs": [],
      }
      
    }
  ]
}
