#!/usr/bin/env bash

for s in $@:
do
cd $s
echo $s
anvi-import-functions -c *contigs.db -i *functions_matrix.txt
anvi-import-taxonomy -c *contigs.db -i *taxonomy_matrix.txt -p 'default_matrix'
cd ..
done
echo 'Done.'
