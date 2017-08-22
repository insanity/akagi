from akagi.data_sources import S3DataSource, RedshiftDataSource

print("Image on S3")
df = S3DataSource.for_prefix(
    'misc-internal.ap-northeast-1',
    'yuichiro-someya/tmp/zebra/')

for d in df:
    print(len(d.read()))

for d in df:
    print(len(d.read()))


print("Redshift (CSV)")
df = RedshiftDataSource('select id, title from (select id, title from cookpad.recipes limit 10)')

for d in df:
    print(d)

for d in df:
    print(d)

print("CSV on S3")
df = S3DataSource.for_prefix(
    'misc-internal.ap-northeast-1',
    'yuichiro-someya/tmp/csv_on_s3/', 'csv')

for d in df:
    print(d)

for d in df:
    print(d)
