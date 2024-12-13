    # .group_by(['regiao', 'forma_pagamento'])
        # .agg((pl.col('quantidade') * pl.col('preco')).sum().alias('total'))