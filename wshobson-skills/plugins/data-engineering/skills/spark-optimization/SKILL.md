---
name: wshobson-spark-optimization
description: Optimize Apache Spark jobs with partitioning, caching, shuffle optimization,
  and memory tuning. Use when improving Spark performance, debugging slow jobs, or
  scaling data processing pipelines.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Apache Spark Optimization

Production patterns for optimizing Apache Spark jobs including partitioning strategies, memory management, shuffle optimization, and performance tuning.

## When to Use This Skill

- Optimizing slow Spark jobs
- Tuning memory and executor configuration
- Implementing efficient partitioning strategies
- Debugging Spark performance issues
- Scaling Spark pipelines for large datasets
- Reducing shuffle and data skew

## Core Concepts

### 1. Spark Execution Model

```
Driver Program
    ↓
Job (triggered by action)
    ↓
Stages (separated by shuffles)
    ↓
Tasks (one per partition)
```

### 2. Key Performance Factors

| Factor            | Impact                | Solution                      |
| ----------------- | --------------------- | ----------------------------- |
| **Shuffle**       | Network I/O, disk I/O | Minimize wide transformations |
| **Data Skew**     | Uneven task duration  | Salting, broadcast joins      |
| **Serialization** | CPU overhead          | Use Kryo, columnar formats    |
| **Memory**        | GC pressure, spills   | Tune executor memory          |
| **Partitions**    | Parallelism           | Right-size partitions         |

## Quick Start

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create optimized Spark session
spark = (SparkSession.builder
    .appName("OptimizedJob")
    .config("spark.sql.adaptive.enabled", "true")
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
    .config("spark.sql.adaptive.skewJoin.enabled", "true")
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    .config("spark.sql.shuffle.partitions", "200")
    .getOrCreate())

# Read with optimized settings
df = (spark.read
    .format("parquet")
    .option("mergeSchema", "false")
    .load("s3://bucket/data/"))

# Efficient transformations
result = (df
    .filter(F.col("date") >= "2024-01-01")
    .select("id", "amount", "category")
    .groupBy("category")
    .agg(F.sum("amount").alias("total")))

result.write.mode("overwrite").parquet("s3://bucket/output/")
```

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices

### Do's

- **Enable AQE** - Adaptive query execution handles many issues
- **Use Parquet/Delta** - Columnar formats with compression
- **Broadcast small tables** - Avoid shuffle for small joins
- **Monitor Spark UI** - Check for skew, spills, GC
- **Right-size partitions** - 128MB - 256MB per partition

### Don'ts

- **Don't collect large data** - Keep data distributed
- **Don't use UDFs unnecessarily** - Use built-in functions
- **Don't over-cache** - Memory is limited
- **Don't ignore data skew** - It dominates job time
- **Don't use `.count()` for existence** - Use `.take(1)` or `.isEmpty()`
