	)YNBim@)YNBim@!)YNBim@	�Ґ�˝�?�Ґ�˝�?!�Ґ�˝�?"h
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails'�	)YNBim@��ګ>e@ARC�ZO@YI*S�Aб?*	���S�U@2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat�ɐc�?!��>�v�?@)=~oӟ��?1и���<@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[1]::ConcatenateT���ݛ?! ���(@@)��7/N|�?1R��	�8@:Preprocessing2S
Iterator::Model::ParallelMap��0{�v�?!�`����.@)��0{�v�?1�`����.@:Preprocessing2F
Iterator::Model6Z�Pۖ?!�:V��:@)���l�?�?1��'R&@:Preprocessing2�
MIterator::Model::ParallelMap::Zip[0]::FlatMap[1]::Concatenate[0]::TensorSlice���S��y?!��.FP�@)���S��y?1��.FP�@:Preprocessing2X
!Iterator::Model::ParallelMap::Zip���հ�?!Wq��_R@)��)t^cw?1�!r��@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensorg��/c?!K9`aN?@)g��/c?1K9`aN?@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapd��A%�?!�>�ObzA@)s�m�B<b?1���B7%@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B73.0 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	��ګ>e@��ګ>e@!��ګ>e@      ��!       "      ��!       *      ��!       2	RC�ZO@RC�ZO@!RC�ZO@:      ��!       B      ��!       J	I*S�Aб?I*S�Aб?!I*S�Aб?R      ��!       Z	I*S�Aб?I*S�Aб?!I*S�Aб?JCPU_ONLY