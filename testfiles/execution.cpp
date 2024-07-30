#define PY_MAJOR_VERSION 3
#undef ENABLE_PYTHON_MODULE
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/builtins/print.hpp>
#include <pythonic/include/operator_/add.hpp>
#include <pythonic/include/operator_/gt.hpp>
#include <pythonic/include/operator_/iadd.hpp>
#include <pythonic/include/time/time.hpp>
#include <pythonic/builtins/print.hpp>
#include <pythonic/operator_/add.hpp>
#include <pythonic/operator_/gt.hpp>
#include <pythonic/operator_/iadd.hpp>
#include <pythonic/time/time.hpp>
namespace __pythran_execution
{
  struct run_test
  {
    typedef void callable;
    ;
    struct type
    {
      typedef typename pythonic::returnable<pythonic::types::none_type>::type result_type;
    }  ;
    inline
    typename type::result_type operator()() const;
    ;
  }  ;
  inline
  typename run_test::type::result_type run_test::operator()() const
  {
    typedef typename pythonic::assignable<long>::type __type0;
    typedef long __type1;
    typedef decltype(pythonic::operator_::add(std::declval<__type0>(), std::declval<__type1>())) __type2;
    typedef typename __combined<__type0,__type2>::type __type3;
    typename pythonic::assignable_noescape<decltype(pythonic::time::functor::time{}())>::type t = pythonic::time::functor::time{}();
    typename pythonic::assignable<typename __combined<__type3,__type1>::type>::type run = 0L;
    while (true)
    {
      if (pythonic::operator_::gt(pythonic::time::functor::time{}(), pythonic::operator_::add(t, 1L)))
      {
        pythonic::builtins::functor::print{}(run);
        run = 0L;
        t = pythonic::time::functor::time{}();
      }
      run += 1L;
    }
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE

static PyMethodDef Methods[] = {

    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "execution",            /* m_name */
    "",         /* m_doc */
    -1,                  /* m_size */
    Methods,             /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#define PYTHRAN_RETURN return theModule
#define PYTHRAN_MODULE_INIT(s) PyInit_##s
#else
#define PYTHRAN_RETURN return
#define PYTHRAN_MODULE_INIT(s) init##s
#endif
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(execution)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
#if defined(GNUC) && !defined(__clang__)
__attribute__ ((externally_visible))
#endif
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(execution)(void) {
    import_array()
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("execution",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.10.0",
                                      "2024-07-22 05:43:05.882070",
                                      "592712493a883878d6ae7f90570878fac45a6419d0a3ea5393fa79511d259791");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif