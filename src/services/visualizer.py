import pandas as pd
import numpy as np
from pathlib import Path
from core.env import SERVER_FILES_ROOT, DEV_MODE
from django.core.exceptions import ValidationError

hier_table_file = 'src/data/versions/2/hier_table.csv'
hier_table_file = Path(hier_table_file) if DEV_MODE else SERVER_FILES_ROOT + hier_table_file

class Visualizer:
    @staticmethod
    def find_clusters(params):
        # IMPORTANT: rectangle angles are left-bottom to rigth-top
        rect = params.get('rect') or ''
        rect = rect.split(',')

        rect = [eval(n)for n in rect] if len(rect) == 4 else []

        cluster_hier = pd.read_csv(hier_table_file)

        if len(rect) == 4:
            [minX, minY, maxX, maxY] = rect

        if len(rect) == 0:
            minX = cluster_hier.X.min()
            maxX = cluster_hier.X.max()
            minY = cluster_hier.Y.min()
            maxY = cluster_hier.Y.max()

        ind = (cluster_hier.X >= minX) & (cluster_hier.X <= maxX) & (cluster_hier.Y >= minY) & (cluster_hier.Y <= maxY)
        hier_items = cluster_hier.loc[ind]

        best_crit = 0
        best_h = 0
        criteria = [8, 0.33]
        CLUST_ID_MIN = 0

        if len(hier_items):
            for h in range(hier_items.shape[1] - 3)[::-1]: # [48, 47, 46, 45, 44, 43, 42, ..., 0 ]
                cluster_nums = len(hier_items[str(h)][hier_items[str(h)] >= CLUST_ID_MIN].unique())
                cluster_vol = hier_items[str(h)].value_counts().iloc[0]

                if (cluster_nums >= criteria[0]) and (cluster_vol <= len(hier_items) * criteria[1]):
                    best_h = h
                    break
                else:
                    if cluster_nums > best_crit:
                        best_crit = cluster_nums
                        best_h = h

        clusters = hier_items[['doc_id', 'X', 'Y', str(best_h)]]

        coordinates = hier_items.doc_id.unique().tolist()

        clusters = clusters.rename(columns = {str(best_h) : 'cluster'})

        if len(clusters) == 0: return {
            'clusters': [],
            'coordinates': coordinates,
            'minX': clusters.X.min() - 0.1,
            'maxX': clusters.X.max() + 0.1,
            'minY': clusters.Y.min() - 0.1,
            'maxY': clusters.Y.max() + 0.1,
        }

        clusterNums = clusters.cluster.unique()

        clusterNums = clusterNums.tolist()

        # clusterNums = [n for n in clusterNums if n >= 10000]

        return {
            'clusters': clusterNums,
            'coordinates': coordinates,
            'minX': clusters.X.min() - 0.1,
            'maxX': clusters.X.max() + 0.1,
            'minY': clusters.Y.min() - 0.1,
            'maxY': clusters.Y.max() + 0.1,
        }
